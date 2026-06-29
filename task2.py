# task 2
print("- - - Welcome you Job Eligibility Portal - - -")

python_skill = input("Are you proficient in Python? (yes/no): ").strip().lower()

experience = int(input("What is his years of exp or project count? :"))

degree_or_bootcamp = input("Does he have a CS degree or a bootcamp? (yes/no) :").strip()

if python_skill == "yes" and (experience >= 2 or degree_or_bootcamp == "yes") :

    print("Congratulations! You've moved to the next interview stage.")
else:
    print("Sorry, your qualifications do not meet the job requirements.")
    