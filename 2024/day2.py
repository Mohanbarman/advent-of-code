reports = []

with open("day2.input", "r") as f:
    for line in f.readlines():
        report = list(map(int, line.split(" ")))
        reports.append(report)


def find_safe_reports(reports: list[list[int]]) -> int:
    safe_reports = 0

    for report in reports:
        is_safe = True
        # report is in increasing order
        if (report[0] - report[1]) < 0:
            for level_index in range(len(report) - 1):
                if not (
                    ((report[level_index + 1] - report[level_index]) >= 1)
                    and ((report[level_index + 1] - report[level_index]) <= 3)
                ):
                    is_safe = False
                    break
        # reports are in decreasing order
        elif (report[0] - report[1]) > 0:
            for level_index in range(len(report) - 1):
                if not (
                    (report[level_index] - (report[level_index + 1]) >= 1)
                    and ((report[level_index] - report[level_index + 1]) <= 3)
                ):
                    is_safe = False
                    break
        else:
            is_safe = False

        if is_safe:
            safe_reports += 1
        print(report, "->", is_safe)

    return safe_reports


def find_safe_reports_2(reports: list[list[int]]) -> int:
    safe_reports = 0

    for report in reports:
        for i in range(len(report)):
            updated_report = report.copy()
            updated_report.pop(i)

            is_safe = True
            # report is in increasing order
            if (updated_report[0] - updated_report[1]) < 0:
                for level_index in range(len(updated_report) - 1):
                    if not (
                        ((updated_report[level_index + 1] - updated_report[level_index]) >= 1)
                        and ((updated_report[level_index + 1] - updated_report[level_index]) <= 3)
                    ):
                        is_safe = False
                        break
            # updated_reports are in decreasing order
            elif (updated_report[0] - updated_report[1]) > 0:
                for level_index in range(len(updated_report) - 1):
                    if not (
                        (updated_report[level_index] - (updated_report[level_index + 1]) >= 1)
                        and ((updated_report[level_index] - updated_report[level_index + 1]) <= 3)
                    ):
                        is_safe = False
                        break
            else:
                is_safe = False

            if is_safe:
                safe_reports += 1
                break

    return safe_reports


print(find_safe_reports_2(reports))
