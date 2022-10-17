import re
import urllib.parse
from os import path

import requests

from model import Problem


def generate_problem_list():
    response = requests.get('https://leetcode.com/api/problems/all/')
    questions = sorted(response.json()[
                       "stat_status_pairs"], key=lambda x: x["stat"]["frontend_question_id"])
    result = []

    for question in questions:
        questionId = question["stat"]["frontend_question_id"]
        problemName = question["stat"]["question__title"]
        problemSlug = question["stat"]["question__title_slug"]
        isPremium = question["paid_only"]
        solutions = []
        normalizedName = re.sub("\s", "_", problemName.lower())
        filePath = f"problems/{normalizedName}"
        difficulty = question["difficulty"]["level"] - 1

        if path.exists(filePath):
            languages = [".py", ".cpp", ".java"]
            for language in languages:
                fullPath = f"{filePath}/solution{language}"
                if path.exists(fullPath):
                    solutions.append(
                        (language[1:], urllib.parse.quote(fullPath)))

        problem = Problem(questionId, problemName, problemSlug,
                          normalizedName, solutions, isPremium, difficulty)
        result.append(problem)

    return result


def write_to_readme(problemList):
    difficultyColorList = [":green_circle:", ":orange_circle:", ":red_circle:"]
    base_url = "https://leetcode.com/problems"
    title = "# Leetcode Solutions"
    leetcode_badge = "[![LeetCode user hwennn](https://img.shields.io/badge/dynamic/json?style=for-the-badge&labelColor=black&color=%23ffa116&label=Solved&query=solvedOverTotal&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2Fhwennn&logo=leetcode&logoColor=yellow)](https://leetcode.com/hwennn/)"
    color_legend = "- :green_circle:: **Easy**\n" + \
        "- :orange_circle:: **Medium**\n" +\
        "- :red_circle:: **Hard**\n"

    table_headers = "[]() | ID | Question | Difficulty  | Solution "
    table_border = ":---: | :---: | --- | :---: | ---"

    with open("README.md", "w") as fp:
        fp.write(title + "\n\n")
        fp.write(leetcode_badge + "\n")
        fp.write(color_legend + "\n")
        fp.write(table_headers + "\n")
        fp.write(table_border + "\n")

        for problem in problemList:
            isCompleted = ":white_check_mark:" if len(
                problem.solutions) > 0 else "[](check)"
            isPremium = ":lock: " if problem.isPremium else ""
            solutions = "<br />".join(
                f"[{language}]({codePath})" for language, codePath in problem.solutions)
            fp.write(
                f"{isCompleted} | {isPremium}{problem.id} | [{problem.name}]({base_url}/{problem.slug}) | {difficultyColorList[problem.difficulty]} \
                        | {solutions} \n"
            )


if __name__ == '__main__':
    problemList = generate_problem_list()
    write_to_readme(problemList)
