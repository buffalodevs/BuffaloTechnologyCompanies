import yaml

def gen():
    print("generating")
    with open("companies.yaml", 'r') as stream:
        try:
            obj = yaml.load(stream)
            companies = obj['companies'] 
            with open('README.md', 'w') as f:
                companies.sort(key=lambda x: x['name'])
                f.write('# Buffalo New York Technology Companies\n\n')
                f.write('An alphabetical list of companies in buffalo who hire developers and other technical folk.\n\n')
                f.write('Feel free to submit pull requests to add any companies.\n\n')
                f.write('| Company | Location | Industry | Tech Stack | Careers |\n')
                f.write('| ------- | -------- | -------- | ---------- | ------- |\n')
                for company in companies:
                    f.write('|' + company['name'])
                    f.write('|' + company['location'])
                    f.write('|' + company['industry'])
                    f.write('|' + company['tech-stack'])
                    if 'careers' in companies:
                        f.write('|' + company['careers'])
                    else:
                        f.write('|')
                    f.write('\n')
        except Exception as e:
            print(e)
            raise e


if __name__ == "__main__":
    gen()
