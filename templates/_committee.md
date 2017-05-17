[back](index.md)

## {{ c['committee']['thomas_id'] }} - {{ c['committee']['name'] }}

{{ c['committee']['jurisdiction'] }}

[link]({{ c['committee']['url'] }})
[minority link]({{ c['committee']['minority_url'] }})

{% for m in c['members'] -%}
{% set member = c['members'][m] %}
### {{ member['name']['official_full'] }}

| state | type | party | url |
|:----- |:---- |:----- |:--- |
| {{ member['term']['state'] }} | {{ member['term']['type'] }} | {{ member['term']['party'] }} | [link]({{ member['term']['url'] }}) |

| phone | address | city | state | zip |
|:----- |:------- |:---- |:----- |:--- |
{%- for f in c['members'][m]['offices'] %}
| {{ f['phone'] }} | {{ f['address'] }} {{ f['building'] }} {{ f['suite'] }} | {{ f['city'] }} | {{ f['state'] }} | {{ f['zip'] }} |
{%- endfor %}

{% endfor %}

