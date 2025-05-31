<!-- # Procedure
1. latest python version install e.g 3.13.3
2. run command python -m venv venv
3. run command .\venv\Script\activate        # (venv) color green
4. pip install openai-agents
5. pip install python-dotenv
6. Now make a file named requirement.txt and write in this file
    (i)  openai-agents
    (ii) python-dotenv

7. pip install -r .\requirements.txt
8. create file .env and write
    OPENAI_API_KEY=XXXXXXXXAPI KEYS HEREXXXXXXXXX

9. create a file for codding e.g main.ipynb and write in this file
    (i)  in first code cell !pip install openai-agents -qU
    (ii) in second cell 
        import os
        from dotenv import load_dotenv

        load_dotenv()
        api-key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Please set the OPENAI_API_KEY environment variable.")
    
    (iii) in third cell 
            from agents import Agents, Runner
            agent = Agent(name="Simple Agent", description="A simple agent that can answer questions.")
            result = await Runner.run(agent, input="What is the capital of France?")
            result.final_output

Now need open api keys to test this code. -->
