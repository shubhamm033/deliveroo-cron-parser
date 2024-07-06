from parsing_type_factory import ParsingTypeFactory

from collections import OrderedDict


class Parser:

    def __init__(self, cron_string):
        self.cron_string = cron_string
        self.field_types = ["minute", "hour", "day_month", "month", "day_week"]

    # Split the cron string into its parts
    def split_and_parse(self):

        cron_string_split = self.cron_string.split(" ")
        if len(cron_string_split) != 6:
            raise ValueError("Invalid cron string format")
        res = OrderedDict()
        for i in range(len(self.field_types)):
            parsing_type = ParsingTypeFactory.get_parsing_strategy(self.field_types[i])
            output = parsing_type.parse(cron_string_split[i])
            res[self.field_types[i]] = output
        res["command"] = cron_string_split[-1]
        return res

    # Format the result in the given output
    @staticmethod
    def format_result(cron_dict):
        output = []
        for field in ["minute", "hour", "day_month", "month", "day_week"]:
            values = ' '.join(map(str, cron_dict[field]))
            output.append(f"{field:<13} {values}")
        output.append(f"command       {cron_dict['command']}")
        return '\n'.join(output)
