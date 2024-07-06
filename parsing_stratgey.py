from abc import ABC, abstractmethod


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
        start = 0
        end = 60
        return self.string_parser(field, start, end)


class HourParsingStrategy(ParsingStrategy):

    def parse(self, field):
        start = 1
        end = 24
        return self.string_parser(field, start, end)


class DayMonthParsingStrategy(ParsingStrategy):

    def parse(self, field):
        start = 1
        end = 30
        return self.string_parser(field, start, end)


class MonthParsingStrategy(ParsingStrategy):

    def parse(self, field):
        start = 1
        end = 12
        return self.string_parser(field, start, end)


class DayOfWeekParsingStrategy(ParsingStrategy):

    def parse(self, field):
        start = 1
        end = 7
        return self.string_parser(field, start, end)
