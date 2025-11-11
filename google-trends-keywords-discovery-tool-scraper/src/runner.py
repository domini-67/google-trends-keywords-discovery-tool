thonimport json
from extractors.google_trends_parser import parse_trends
from outputs.exporters import export_to_json

def main():
    with open('data/inputs.sample.json') as f:
        data = json.load(f)

    keyword = data.get('keyword')
    if not keyword:
        raise ValueError("No keyword found in the input data")

    trends_data = parse_trends(keyword)
    export_to_json(trends_data, 'data/sample_output.json')

if __name__ == '__main__':
    main()