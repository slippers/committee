{% for c in comm %}
* [{{ c['committee']['name'] }}](#{{ c['committee']['thomas_id'] }})
{%- endfor %}


{% for c in comm %}
---
## <a name="{{ c['committee']['thomas_id'] }}"></a> {{ c['committee']['name'] }}

{{ c['committee']['jurisdiction'] }}

{% for m in c['members'] -%}
{% set member = c['members'][m] %}
### {{ member['name']['official_full'] }}

| state | type | party |
|:----- |:---- |:----- |
| {{ member['term']['state'] }} | {{ member['term']['type'] }} | {{ member['term']['party'] }} |

| phone | address | city | state | zip |
|:----- |:------- |:---- |:----- |:--- |
{%- for f in c['members'][m]['offices'] %}
| {{ f['phone'] }} | {{ f['address'] }} {{ f['building'] }} {{ f['suite'] }} | {{ f['city'] }} | {{ f['state'] }} | {{ f['zip'] }} |
{%- endfor %}

{% endfor %}
{% endfor %}
