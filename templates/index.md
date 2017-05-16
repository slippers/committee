{% for c in comm %}
* [{{ c['committee']['name'] }}]({{ c['committee']['thomas_id'] }}.md)
{%- endfor %}
