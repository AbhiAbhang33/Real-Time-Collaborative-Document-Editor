import requests


def check_grammar(text):
    try:
        response = requests.post(
            'https://api.languagetool.org/v2/check',
            data={'text': text, 'language': 'en-US'},
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        if response.status_code == 200:
            matches = response.json().get('matches', [])
            suggestions = []
            for match in matches:
                suggestion = {
                    'message': match['message'],
                    'replacement': match['replacements'][0]['value'] if match['replacements'] else '',
                    'category': match['rule']['category']['name']
                }
                suggestions.append(suggestion)
            return suggestions
    except Exception as e:
        print("Grammar API exception:", str(e))
    return []
