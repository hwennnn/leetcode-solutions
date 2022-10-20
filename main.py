import json
import re
import urllib.parse
from fileinput import filename
from os import makedirs, path

import requests

from model import Problem
from utils import get


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

        readmePath = f"problems/{normalizedName}/README.md"

        if not path.exists(readmePath) and not isPremium:
            problemDetails = fetch_problem(problemSlug)
            write_desc_to_readme(problemDetails)

        problem = Problem(questionId, problemName, problemSlug,
                          normalizedName, solutions, isPremium, difficulty)
        result.append(problem)

    return result


def fetch_problem(slug):
    query_params = {
        'operationName': "getQuestionDetail",
        'variables': {'titleSlug': slug},
        'query': '''query getQuestionDetail($titleSlug: String!) {
                            question(titleSlug: $titleSlug) {
                                questionId
                                questionFrontendId
                                questionTitle
                                questionTitleSlug
                                content
                                difficulty
                                stats
                                similarQuestions
                                categoryTitle
                                topicTags {
                                name
                                slug
                            }
                        }
                    }'''
    }

    resp = requests.post(
        "https://leetcode.com/graphql",
        data=json.dumps(query_params).encode('utf8'),
        headers={
            "content-type": "application/json",
        })
    body = json.loads(resp.content)

    # parse data
    question = get(body, 'data.question')
    question["normalized_title"] = re.sub(
        "\s", "_", question["questionTitle"].lower())

    display_id = question['questionFrontendId']
    title = question["questionTitle"]
    normalizedTitle = question["normalized_title"]
    level = question["difficulty"]
    description = question['content']
    topics = question['topicTags']
    link = "https://leetcode.com/problems/" + slug

    data = {
        "id": display_id,
        "title": title,
        "slug": slug,
        "normalized_title": normalizedTitle,
        "level": level,
        "description": description,
        "topics": topics,
        "link": link,
    }

    filename = f"problems/{normalizedTitle}/data.json"
    makedirs(path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(question, f)

    return data


def write_desc_to_readme(problem):
    print(problem["id"], problem["title"])
    with open('templates/PROBLEM_README.md') as f:
        contents = f.read()
        contents = contents.replace(
            "question_description", problem["description"])
        contents = contents.replace("question_id", problem["id"])
        contents = contents.replace("question_title", problem["title"])
        contents = contents.replace(
            "question_link", problem["link"])

        difficulty_badge = f"https://img.shields.io/badge/Difficulty-{problem['level']}-blue.svg"
        contents = contents.replace("question_difficulty", difficulty_badge)

        formattedTopics = ", ".join(
            topic["name"] for topic in list(problem["topics"]))
        formattedTopics = formattedTopics.replace("-", " ")
        topics = f"https://img.shields.io/badge/Topics-{formattedTopics}-orange.svg"
        topics = topics.replace(" ", "%20")
        contents = contents.replace("question_topics", topics)

        filename = "problems/" + problem["normalized_title"] + "/README.md"
        makedirs(path.dirname(filename), exist_ok=True)
        with open(filename, "w") as fp:
            fp.write(contents)


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
