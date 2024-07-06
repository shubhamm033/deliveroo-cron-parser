from parsing_stratgey import MonthParsingStrategy, DayMonthParsingStrategy, \
    DayOfWeekParsingStrategy, MinuteParsingStrategy, HourParsingStrategy


class ParsingTypeFactory:

    @staticmethod
    def get_parsing_strategy(type):
        if type == "minute":
            return MinuteParsingStrategy()
        elif type == "hour":
            return HourParsingStrategy()
        elif type == "day_month":
            return DayMonthParsingStrategy()
        elif type == "month":
            return MonthParsingStrategy()
        elif "day_week":
            return DayOfWeekParsingStrategy()
