from abc import ABC, abstractmethod

from config import field_ranges


class ParsingStrategy(ABC):

    @abstractmethod
    def parse(self, field):
        pass

    def string_parser(self, field, start, end):

        all_range = list(range(start, end + 1))

        if field == "*":
            return all_range

        elif "," in field:
            parts = field.split(",")

            return list(map(int, parts))

        elif "/" in field:
            base, interval = field.split("/")

            if "*" in base:

                r = [start, end]

                return [i for i in range(r[0], r[-1], int(interval))]

            elif "-" in base:
                temp = base.split("-")

                r = [int(temp[0]), int(temp[1]) + 1]

                return [i for i in range(r[0], r[-1], int(interval))]

        elif "-" in field:
            temp = field.split("-")

            return list(range(int(temp[0]), int(temp[1]) + 1))

        else:
            return [int(field)]


class MinuteParsingStrategy(ParsingStrategy):

    def parse(self, field):
        minute_range = field_ranges.get("minute")
        start = minute_range[0]
        end = minute_range[1]
        return self.string_parser(field, start, end)


class HourParsingStrategy(ParsingStrategy):

    def parse(self, field):
        hour_range = field_ranges.get("hour")
        start = hour_range[0]
        end = hour_range[1]
        return self.string_parser(field, start, end)


class DayMonthParsingStrategy(ParsingStrategy):

    def parse(self, field):
        day_month_range = field_ranges.get("day_month")
        start = day_month_range[0]
        end = day_month_range[1]
        return self.string_parser(field, start, end)


class MonthParsingStrategy(ParsingStrategy):

    def parse(self, field):
        month_range = field_ranges.get("month")
        start = month_range[0]
        end = month_range[1]
        return self.string_parser(field, start, end)


class DayOfWeekParsingStrategy(ParsingStrategy):

    def parse(self, field):
        day_week_range = field_ranges.get("day_week")
        start = day_week_range[0]
        end = day_week_range[1]
        return self.string_parser(field, start, end)
