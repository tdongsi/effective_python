import json

UNDEFINED = object()


def divide_json(path):
    handle = open(path, 'r+')  # IOError
    try:
        data = handle.read()    # UnicodeDecodeError
        op = json.loads(data)   # Value Error
        value = op['numerator'] / op['denominator']     # ZeroDivisionError
    except:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()


def main():
    temp_path = '/tmp/random_data.json'
    with open(temp_path, 'w') as handle:
        handle.write('{"numerator":1.0, "denominator":2}')

    print divide_json(temp_path)
    pass


if __name__ == '__main__':
    main()