
class InvalidInputException(Exception):
    pass


single_number_mapper = {
    "0": "nul",
    "1": "en",
    "2": "to",
    "3": "tre",
    "4": "fire",
    "5": "fem",
    "6": "seks",
    "7": "syv",
    "8": "otte",
    "9": "ni",
    "10": "ti",
    "11": "elleve",
    "12": "tolv",
    "13": "tretten",
    "14": "fjorten",
    "15": "femten",
    "16": "seksten",
    "17": "sytten",
    "18": "atten",
    "19": "nitten",
    "20": "tyve",
    "30": "tredive",
    "40": "fyrre",
    "50": "halvtreds",
    "60": "treds",
    "70": "halvfjerds",
    "80": "firs",
    "90": "halvfems"
}


def under_100(number, int_number):
    # 1-10 og 20,30, ... , 90
    if number in single_number_mapper:
        return single_number_mapper[number]

    # base number
    base = str(int_number % 10)

    # tens
    tens = number[0] + "0"

    return single_number_mapper[base] + "og" + single_number_mapper[tens]


def mapper_100s(int_number):
    pre = single_number_mapper[str(int(int_number / 100))]
    if pre == "en":
        pre = ""

    int_post_number = int(int_number % 100)
    post_number = str(int_post_number)

    post = under_100(post_number, int_post_number)
    if post == "nul":
        post = ""
    else:
        post = " og " + post

    return pre + "hundrede" + post


def mapper_1000s(int_number):
    pre = number_to_text_mapper(int(int_number / 1000))
    if pre == "en":
        pre = ""
    else:
        pre = pre + " "

    post_number = int(int_number % 1000)
    post = number_to_text_mapper(post_number)
    if post_number < 100:
        post = " og " + post
    else:
        post = " " + post

    return pre + "tusinde" + post


def mapper_millions(int_number):
    pre = number_to_text_mapper(int(int_number / 1000000))

    if pre == "en":
        pre = "million"
    else:
        pre = pre + " millioner"

    post_number = int(int_number % 1000000)
    post = number_to_text_mapper(post_number)

    if post_number == 0:
        post = ""
    else:
        post = " " + post

    return pre + post


def number_to_text_mapper(number):
    """
    Converts a number to a string representation in Danish

    :param number: int or string representing the number to be converted
    :return: string representation of number
    """
    try:
        number = str(int(number))
    except ValueError:
        raise InvalidInputException("Please provide a valid number as either integer or string")

    int_number = int(number)
    num_length = len(number)

    # under 100
    if num_length < 3:
        return under_100(number, int_number)

    # hundreds
    if num_length == 3:
        return mapper_100s(int_number)

    # thousands
    if num_length < 7:
        return mapper_1000s(int_number)

    # millions
    if num_length < 10:
        return mapper_millions(int_number)

    # billion
    if num_length == 10:
        return "en milliard"

    # More than billion is invalid input
    if num_length > 10:
        raise InvalidInputException("Mapper only supports numbers from 0 to 1.000.000.000 (inclusive)")


if __name__ == '__main__':
    n = "21021240"
    print(number_to_text_mapper(n))
