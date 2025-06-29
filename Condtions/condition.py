# Learning Conditions in Python
# This code snippet demonstrates how to create a simple condition in Python to check if a person is eligible to vote based on their age.

def print_name():
    name=input("\nPlease enter your name: ")
    print(f"\nHello, {name}! Welcome to my Website.")

# This function prompts the user to enter their name and then prints a greeting message.

print_name()

Devops=["jenkins", "docker", "kubernetes", "ansible", "terraform"]
Development=["python", "java", "javascript", "c++", "c#"]
softskills=["communication", "teamwork", "problem-solving", "adaptability", "time management"]
soft_skills = {
    "emotional intelligence": "Ability to understand and manage your own emotions and those of others",
    "critical thinking": "Ability to analyze facts to form a judgment",
    "leadership": "Ability to inspire, guide, and influence others",
    "work ethic": "Demonstrating dedication, responsibility, and professionalism",
    "creativity": "Ability to think outside the box and generate innovative ideas",
    "conflict resolution": "Ability to mediate disagreements and find peaceful solutions",
    "interpersonal skills": "Ability to build and maintain positive relationships with others",
    "resilience": "Ability to bounce back from setbacks and remain persistent",
    "attention to detail": "Thoroughness and accuracy in accomplishing tasks",
    "active listening": "Fully concentrating, understanding, and responding thoughtfully in conversations"
}

skill_set = input("\nPlease enter your skill set (devops, development, softskills): ").strip().lower()

if skill_set in Devops:
    print(f"\nYou have selected DevOps skills: {skill_set}.")
elif skill_set in Development:
    print(f"\nYou have selected Development skills: {skill_set}.")
elif skill_set in softskills:
    print(f"\nYou have selected Soft Skills: {skill_set}.")

elif skill_set in soft_skills:
    print(f"\nYou have selected Soft Skills: {skill_set}.")
    print(f"Description: {soft_skills[skill_set]}")

else:
    print(f"\nThe skill set '{skill_set}' is not recognized. Please choose from DevOps, Development, or Soft Skills.")

# [] is used to create a list in Python, which is a collection of items that can be of different types.
# {} is used to create a dictionary in Python, which is a collection of key-value pairs
# () is used to create a tuple in Python, which is similar to a list but is immutable (cannot be changed after creation).