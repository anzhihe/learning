
from string import Template

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '">')

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

def radio_button_id(rb_name, rb_value, rb_id):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + str(rb_id) + '"> ' + rb_value + '<br />')

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    return('<p>' + para_text + '</p>')

def create_inputs(inputs_list):
    html_inputs = ''
    for each_input in inputs_list:
        html_inputs = html_inputs + '<input type="Text" name="' + each_input + '" size=40>'
    return(html_inputs)

def do_form(name, the_inputs, method="POST", text="Submit"):
    with open('templates/form.html') as formf:
        form_text = formf.read()
    inputs = create_inputs(the_inputs)
    form = Template(form_text)
    return(form.substitute(cgi_name=name,
                           http_method=method,
                           list_of_inputs=inputs,
                           submit_text=text))
