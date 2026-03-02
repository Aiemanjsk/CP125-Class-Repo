def match_specialists(candidates_list, project_requirements):
    skill_frequency = {}
    
    for _, skills in candidates_list:
        for skill in skills:
            skill_frequency[skill] = skill_frequency.get(skill, 0) + 1

    # Step 2: Identify rare skills (held by < 3 people)
    rare_skills = {
        skill for skill, count in skill_frequency.items()
        if count < 3
    }

    # Step 3: Find matching specialists
    specialists = []

    for name, skills in candidates_list:
        # Check if candidate meets all project requirements
        if project_requirements.issubset(skills):
            # Find this candidate's rare skills
            candidate_rare_skills = skills.intersection(rare_skills)
            
            if candidate_rare_skills:
                specialists.append((name, candidate_rare_skills))

    return specialists
    pass
