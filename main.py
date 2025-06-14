import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

from prompts import extraction_prompt, email_prompt

#Load env variables from .env 
load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")

#Initialize LLM for analyzing transcripts and generating personalized emails
#Temperature = 0.7 for a balance between creativity and accuracy
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=api_key, temperature=0.7) 

#Create chain for extracting key information from counseling transcripts
extract_chain = LLMChain(llm=llm, prompt=extraction_prompt)

#Create a chain for generating personalized follow-up emails
email_chain = LLMChain(llm=llm, prompt=email_prompt)

#Simulating sending an email by printing to console
def send_mock_email(to_email, subject, body):
    print("\nSending email to:", to_email)
    print("Subject:", subject)
    print("Body:\n", body)

def main():
    print("Welcome to the Counseling Follow-Up Generator!\n")

    # Collect student name 
    student_name = input("Enter the student's name: ")

    # Collect session transcript through multi-line input
    #User can terminate input by pressing Enter twice
    print("\nPaste the counseling transcript (press enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    transcript = "\n".join(lines)

    #Process the transcript to extract career goals and action items
    print("\nExtracting key takeaways...")
    takeaways = extract_chain.invoke({"transcript": transcript})
    print("\nTakeaways:\n", takeaways["text"])

    #Generate personalized email based on the extracted information
    print("\nGenerating email...")
    email = email_chain.invoke({
        "student_name": student_name,
        "takeaways": takeaways["text"]
    })
    email_text = email["text"]

    # Collect recipient email and display the generated email
    to_email = input("Enter recipient email (can be fake): ")
    subject = f"Your Career Counseling Follow-Up, {student_name}"
    send_mock_email(to_email, subject, email_text)

if __name__ == "__main__":
    main()
