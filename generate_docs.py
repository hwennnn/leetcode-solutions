import json
from os import makedirs, path, walk


def main():
    template = open("templates/DOCS_TEMPLATE.md", "r").read()
    problemsDir = "./problems"

    for subdir, _, _ in walk(problemsDir):
        jsonPath = f"{subdir}/data.json"

        if not path.exists(jsonPath):
            continue

        contents = template
        data = json.load(open(jsonPath, "r"))
        problemID = data["questionFrontendId"]
        problemTitle = data["questionTitle"]
        problemSlug = data["questionTitleSlug"]
        problemDescription = data["content"]

        contents = contents.replace("{PROBLEM_ID}", problemID)
        contents = contents.replace("{PROBLEM_TITLE}", problemTitle)
        contents = contents.replace("{PROBLEM_SLUG}", problemSlug)
        contents = contents.replace(
            "{PROBLEM_DESCRIPTION}", problemDescription)

        problemDifficulty = data["difficulty"]
        problemTopics = data["topicTags"]

        difficulty_badge = f"https://img.shields.io/badge/Difficulty-{problemDifficulty}-blue.svg"
        contents = contents.replace("question_difficulty", difficulty_badge)

        formattedTopics = ", ".join(
            topic["name"] for topic in list(problemTopics))
        formattedTopics = formattedTopics.replace("-", " ")
        topics = f"https://img.shields.io/badge/Topics-{formattedTopics}-orange.svg"
        topics = topics.replace(" ", "%20")
        contents = contents.replace("question_topics", topics)

        codeTemplate = "``` {LANGUAGE} title='{PROBLEM_SLUG}{LANGUAGE}'\n{CODE}\n```\n"
        solutions = ""

        for language in [".py", ".java", ".cpp"]:
            codePath = f"{subdir}/solution{language}"

            if path.exists(codePath):
                code = open(codePath, "r").read()
                solutions += codeTemplate.replace("{PROBLEM_SLUG}", problemSlug).replace("{LANGUAGE}",
                                                                                         language).replace("{CODE}", code) + "\n"
        contents = contents.replace("{PROBLEM_SOLUTIONS}", solutions)

        filename = "docs/" + f"/{problemID.zfill(4)}.md"
        makedirs(path.dirname(filename), exist_ok=True)
        with open(filename, "w") as fp:
            fp.write(contents)


if __name__ == "__main__":
    main()
