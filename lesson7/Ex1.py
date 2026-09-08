survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++"  "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"]
]

choices_srts = [set(p) for p in survey_results]
common_languages = set.intersection(*choices_srts)
print("1. Languages chosen by all participants:", common_languages)

all_languages = set.union(*choices_srts)

#?
unique_languages = len(all_languages)
print("3. Number of unique languages:", unique_languages)

