analysis : str = input("Write something: ")

analysis_type = analysis.__class__
analysis_length = len(analysis)
is_space  = analysis.isspace()
is_number = analysis.isnumeric()
is_alpha = analysis.isalpha()
is_alnum = analysis.isalnum()
is_upper = analysis.isupper()
is_lower = analysis.islower()
is_title = analysis.istitle()

print(f"Class type: {analysis_type}\nNumber of letters: {analysis_length}\nOnly has spaces? {is_space}\nNumbers only? {is_number}\nIs it alphabetical? {is_alpha}\nIs it alpha-numeric? {is_alnum}\nIs it uppercase? {is_upper}\nIs it lowercase? {is_lower}\nIs it capitalized? {is_title}")

