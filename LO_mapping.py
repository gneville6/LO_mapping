from IPython.display import HTML, display


# Function to input and store learning objectives
def get_learning_objectives():
  objectives_input = input("Enter Learning Objectives (separated by lines or periods):\n")
  # Replace periods with line breaks for consistent processing:
  objectives_input = objectives_input.replace('.', '\n')
  objectives = [obj.strip() for obj in objectives_input.split('\n') if obj.strip()]
  print(f"\nYou have entered {len(objectives)} Learning Objectives:")
  for i, obj in enumerate(objectives, 1):
    print(f"{i}. {obj}")
  if not objectives:  # Check if the list is empty
      print("Error: Please enter at least one learning objective.")
  return objectives

# Function to input and store assignments
def get_assignments():
    assignments_input = input("Enter Assignments (separated by lines or semicolons):\n")
    # Replace semicolons with line break for consistent processing:
    assignments_input = assignments_input.replace(';', '\n')
    assignments = [assignment.strip() for assignment in assignments_input.split('\n') if assignment.strip()]
    print(f"\nYou have entered {len(assignments)} Assignments:")
    for i, obj in enumerate(assignments, 1):
      print(f"{i}. {obj}")
    if not assignments:  # Check if the list is empty
      print("Error: Please enter at least one assignment.")
    return assignments

# Function to link assignments to learning objectives
def match_assignments_to_objectives(assignments, objectives):
    assignment_links = {obj: [] for obj in objectives}
    # Print the Learning Objectives list once at the beginning
    print("\nAvailable Learning Objectives:")
    for i, obj in enumerate(objectives, 1):
        print(f"{i}. {obj}")
    for assignment in assignments:
        print(f"\nWhich Learning Objectives does '{assignment}' meet? (Separate multiple objectives by commas, refer to numbers above)")
        selected = input("Enter the numbers of the objectives (or press Enter to skip): ")
        selected_indexes = [int(idx.strip()) - 1 for idx in selected.split(",") if idx.strip().isdigit()]
        try:
            selected_indexes = [int(idx.strip()) - 1 for idx in selected.split(",") if idx.strip().isdigit()]
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers corresponding to the objectives.")
            continue  # Skip to the next assignment
        # This is the missing part:
        for idx in selected_indexes:
            if 0 <= idx < len(objectives):
                assignment_links[objectives[idx]].append(assignment)  # Link assignment to objective

    return assignment_links

# Function to summarize the results
def summarize_links(assignment_links, assignments):
    print("\nSummary of Assignments Linked to Learning Objectives:")
    for obj, linked_assignments in assignment_links.items():
        # Check if there are any linked assignments for this objective:
        if linked_assignments:
            print(f"Objective '{obj}': {len(linked_assignments)} assignment(s) linked")
        else:
            print(f"Objective '{obj}': No assignments linked to this objective.")

    objectives_without_assignments = find_objectives_without_assignments(assignment_links)
    if objectives_without_assignments:
        print("\nObjectives without Assignments:")
        for obj in objectives_without_assignments:
            print(f"- {obj}")

    assignments_without_objectives = find_assignments_without_objectives(assignments, assignment_links)
    if assignments_without_objectives:
        print("\nAssignments without Objectives:")
        for assignment in assignments_without_objectives:
            print(f"- {assignment}")

    print("\nSummary completed.")

    # Check if all Learning Objectives have at least one linked assignment
    all_objectives_have_assignments = all(assignment_links.values()) # Check if all values (lists of assignments) are non-empty

    if all_objectives_have_assignments:
        print("\nAll Learning Objectives have at least one linked assignment.")
    else:
        print("\nWARNING: Some Learning Objectives do not have any linked assignments.")

def find_objectives_without_assignments(assignment_links):
    objectives_without_assignments = []
    for obj, linked_assignments in assignment_links.items():
        if not linked_assignments:  # If the list of linked assignments is empty
            objectives_without_assignments.append(obj)
    return objectives_without_assignments

def find_assignments_without_objectives(assignments, assignment_links):
    all_linked_assignments = [assignment for linked_assignments in assignment_links.values() for assignment in linked_assignments]
    assignments_without_objectives = [assignment for assignment in assignments if assignment not in all_linked_assignments]
    return assignments_without_objectives

def summarize_links(assignment_links, assignments):
    display("Summary of Assignments Linked to Learning Objectives:")
    for obj, linked_assignments in assignment_links.items():
        if linked_assignments:
            assignment_list = ''.join([f'\n\t\t\t*{assignment}' for assignment in (linked_assignments)])
            display(f"Objective '{obj}': {len(linked_assignments)} assignment(s) linked {assignment_list}")

        else:
            display(HTML(f"Objective '\n{obj}': No assignments linked to this objective.")) # Red text
    # Find and display assignments without objectives in red
    all_linked_assignments = [assignment for linked_assignments in assignment_links.values() for assignment in linked_assignments]
    assignments_without_objectives = [assignment for assignment in assignments if assignment not in all_linked_assignments]

    if assignments_without_objectives:
        display("Assignments without Objectives: \n")
        assignment_list = ''.join([f'*{assignment} \n' for assignment in assignments_without_objectives])
        display(HTML(f"{assignment_list}")) # Red text for assignments

# Main function to run the program
def main():
    class_name = input("Enter the Class Name: ")  # Get class name input
    print(f"Course Learning Objective Assignment Matcher for {class_name}")  # Include class name in output
    objectives = get_learning_objectives()
    assignments = get_assignments()
    assignment_links = match_assignments_to_objectives(assignments, objectives)
    summarize_links(assignment_links, assignments) # Modified to pass assignments to summarize_links   1


# Run the program
if __name__ == "__main__":
    main()