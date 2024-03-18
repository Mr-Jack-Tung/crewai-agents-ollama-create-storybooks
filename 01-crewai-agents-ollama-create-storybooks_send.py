
# Create Illustrated Storybooks Instantly with Crew AI Agents! (Groq)
# https://www.youtube.com/watch?v=vWukuS48RbY
# https://mer.vin/2024/03/crewai-groq-create-story-books/
# https://blog.langchain.dev/crewai-unleashed-future-of-ai-agent-teams/

# pip install crewai
# pip install -U 'crewai[tools]' mdpdf

import sys
from crewai import Agent, Task, Crew, Process
from crewai_tools import tool
from langchain_openai import ChatOpenAI
from crewai_tools.tools import FileReadTool
import os, requests, re, mdpdf, subprocess
from openai import OpenAI

from langchain_core.messages import HumanMessage, SystemMessage

# llm = ChatOpenAI(
#     openai_api_base="https://api.groq.com/openai/v1", # https://api.openai.com/v1 or https://api.groq.com/openai/v1 
#     openai_api_key=os.getenv("GROQ_API_KEY"), # os.getenv("OPENAI_API_KEY") or os.getenv("GROQ_API_KEY")
#     model_name="mixtral-8x7b-32768" #  gpt-4-turbo-preview or mixtral-8x7b-32768 
# )

## Ollama
llm = ChatOpenAI(
    openai_api_base="http://localhost:11434/v1", # https://api.openai.com/v1 or https://api.groq.com/openai/v1 
    openai_api_key="Null", # os.getenv("OPENAI_API_KEY") or os.getenv("GROQ_API_KEY")
    model_name="mistral" #  gpt-4-turbo-preview or mixtral-8x7b-32768
)

file_read_tool = FileReadTool(
	file_path='template.md',
	description='A tool to read the Story Template file and understand the expected output format.'
)


@tool
def convermarkdowntopdf(markdownfile_name: str) -> str:
    """
    Converts a Markdown file to a PDF document using the mdpdf command line application.

    Args:
        markdownfile_name (str): Path to the input Markdown file.

    Returns:
        str: Path to the generated PDF file.
    """
    output_file = os.path.splitext(markdownfile_name)[0] + '.pdf'
    
    # Command to convert markdown to PDF using mdpdf
    cmd = ['mdpdf', '--output', output_file, markdownfile_name]
    
    # Execute the command
    subprocess.run(cmd, check=True)
    
    return output_file

story_outliner = Agent(
  role='Story Outliner',
  goal='Develop an outline for a children\'s storybook about Animals, including chapter titles and characters for 5 chapters.',
  backstory="An imaginative creator who lays the foundation of captivating stories for children.",
  verbose=True,
  llm=llm,
  allow_delegation=False
)

story_writer = Agent(
  role='Story Writer',
  goal='Write the full content of the story for all 5 chapters, each chapter 100 words, weaving together the narratives and characters outlined.',
  backstory="A talented storyteller who brings to life the world and characters outlined, crafting engaging and imaginative tales for children.",
  verbose=True,
  llm=llm,
  allow_delegation=False
)

content_formatter = Agent(
    role='Content Formatter',
    goal='Format the written story content in markdown.',
    backstory='A meticulous formatter who enhances the readability and presentation of the storybook.',
    verbose=True,
    llm=llm,
    tools=[file_read_tool],
    allow_delegation=False
)

markdown_to_pdf_creator = Agent(
    role='PDF Converter',
    goal='Convert the Markdown file to a PDF document. story.md is the markdown file name.',
    backstory='An efficient converter that transforms Markdown files into professionally formatted PDF documents.',
    verbose=True,
    llm=llm,
    tools=[convermarkdowntopdf],
    allow_delegation=False
)


# Create tasks for the agents
task_outline = Task(
    description='Create an outline for the children\'s storybook about Animals, detailing chapter titles and character descriptions for 5 chapters.',
    agent=story_outliner,
    expected_output='A structured outline document containing 5 chapter titles, with detailed character descriptions and the main plot points for each chapter.'
)

task_write = Task(
    description='Using the outline provided, write the full story content for all chapters, ensuring a cohesive and engaging narrative for children. Each Chapter 100 words. Include Title of the story at the top.',
    agent=story_writer,
    expected_output='A complete manuscript of the children\'s storybook about Animals with 5 chapters. Each chapter should contain approximately 100 words, following the provided outline and integrating the characters and plot points into a cohesive narrative.'
)

task_format_content = Task(
    description='Format the story content in markdown.',
    agent=content_formatter,
    expected_output='The entire storybook content formatted in markdown, with each chapter title followed by the corresponding the chapter content.',
    context=[task_write], 
    output_file="story.md"
)

task_markdown_to_pdf = Task(
    description='Convert a Markdown file to a PDF document, ensuring the preservation of formatting, structure using the mdpdf library.',
    agent=markdown_to_pdf_creator,
    expected_output='A PDF file generated from the Markdown input, accurately reflecting the content with proper formatting. The PDF should be ready for sharing or printing.'
)

crew = Crew(
  agents=[story_outliner, story_writer, content_formatter, markdown_to_pdf_creator], # image_generator
  tasks=[task_outline, task_write, task_format_content, task_markdown_to_pdf], # task_image_generate
  verbose=True,
  process=Process.sequential
)

result = crew.kickoff()

print(result)
