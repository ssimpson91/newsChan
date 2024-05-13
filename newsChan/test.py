import asyncio
import sys
from search_news import search_news

async def main():
    # Get the topic from the command line arguments or use a default if none provided
    topic = sys.argv[1] if len(sys.argv) > 1 else "default topic"
    max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 2  # Optionally handle max_results from command line

    results = await search_news(topic, max_results)
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
