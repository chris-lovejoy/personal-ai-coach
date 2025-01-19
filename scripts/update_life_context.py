import os
import glob
from datetime import datetime
import anthropic
from dotenv import load_dotenv
import argparse
import frontmatter
import yaml

load_dotenv()

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Update personal AI coach context based on recent conversations.')
    parser.add_argument(
        '-n', '--num-conversations',
        type=int,
        default=3,
        help='Number of most recent conversations to analyze (default: 3)'
    )
    return parser.parse_args()

def load_current_context(base_dir):
    """Load the current context file, separating YAML frontmatter from content."""
    context_path = os.path.join(base_dir, "Life Context Prompts", "Personal AI Coach with Life Context.md")
    
    if not os.path.exists(context_path):
        raise Exception(f"Context file not found: {context_path}")
    
    with open(context_path, 'r', encoding='utf-8') as file:
        post = frontmatter.load(file)
        
    return context_path, post.metadata, post.content


def load_conversations(conversations_dir, num_conversations):
    """Load and parse the most recent conversation files."""
    conversation_files = glob.glob(os.path.join(conversations_dir, "*.md"))
    
    if not conversation_files:
        raise Exception("No conversation files found")
    
    conversation_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    
    conversations = []
    for file_path in conversation_files[:num_conversations]:
        with open(file_path, 'r', encoding='utf-8') as file:
            conversations.append({
                'content': file.read(),
                'date': datetime.fromtimestamp(os.path.getmtime(file_path))
            })
    
    return conversations

def update_context_with_llm(current_context, recent_conversations, client):
    """Use LLM to analyze conversations and update the context."""
    
    system_prompt = """You are an expert at analyzing coaching conversations and extracting relevant context about the client.
    Please analyze the provided conversations and current context, then generate an updated version that:
    1. Maintains exactly the same structure and headings as the current context
    2. Updates the content under each heading based on new information from the conversations
    3. Retains all existing information that remains relevant
    4. Returns the complete context with all sections, even if some weren't updated
    5. Do not drop any information that is relevant - return it all in your response"""
    
    conversations_text = "\n\n".join([
        f"Conversation from {conv['date'].strftime('%Y-%m-%d')}:\n{conv['content']}"
        for conv in recent_conversations
    ])
    
    message = f"""Current context:
    {current_context}
    
    Recent conversations to analyze:
    {conversations_text}
    
    Please provide an updated version of the context incorporating relevant new information from these conversations.
    Maintain exactly the same structure and formatting. Return ALL content (eg. don't say "previous information in this section unchanged").
    """
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=8192,
        temperature=0,
        system=system_prompt,
        messages=[{"role": "user", "content": message}]
    )
    
    return response.content[0].text

def save_updated_context(context_path, current_frontmatter, current_context, updated_context):
    """Archive current context and save the updated version, preserving frontmatter."""
    # Create archive directory if it doesn't exist
    archive_dir = os.path.join(os.path.dirname(context_path), "archive")
    os.makedirs(archive_dir, exist_ok=True)
    
    # Save current version to archive with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_path = os.path.join(
        archive_dir,
        f"Personal AI Coach with Life Context_{timestamp}.md"
    )
    
 # Format the frontmatter as YAML
    frontmatter_yaml = "---\n" + yaml.dump(current_frontmatter, default_flow_style=False) + "---\n"
    
    # Combine frontmatter with content for saving
    full_current_content = frontmatter_yaml + current_context
    full_updated_content = frontmatter_yaml + updated_context

    # Save current version to archive
    with open(archive_path, 'w', encoding='utf-8') as file:
        file.write(full_current_content)
    
    # Save updated version to original location
    with open(context_path, 'w', encoding='utf-8') as file:
        file.write(full_updated_content)
        
def main():
    args = parse_arguments()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)  # Go up one directory
    conversations_dir = os.path.join(base_dir, "Conversations")
    
    client = anthropic.Anthropic()
    
    try:
        # Load recent conversations
        recent_conversations = load_conversations(conversations_dir, args.num_conversations)
        print(f"Loaded {len(recent_conversations)} recent conversations")
        
        # Load current context
        context_path, current_frontmatter, current_context = load_current_context(base_dir)
        print("Loaded current context")
        
        # Update context using LLM
        print("Updating context with LLM (may take a minute or two)...")
        updated_context = update_context_with_llm(
            current_context,
            recent_conversations,
            client
        )
        print("Updated context generated")
        
        # Save the updated context
        save_updated_context(context_path, current_frontmatter, current_context, updated_context)
        print("Successfully updated and archived the context")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
