from typing import Optional
from .snow_class import SnowConnection


class BaseValidator:
    conn: SnowConnection
    query_base = """
        SELECT
            {% for column in columns %}
                 {{'' if loop. first else ', '}}{{column}}
            {% endfor %}
        FROM {{table}}
        {% if where %}
            where
            {% for condition in where %}
                 {{'' if loop. first else 'AND '}}{{condition}}
            {% endfor %}
        {% endif %}
        {% if group_by %}
            group by
            {% for condition in group_by %}
                 {{'' if loop. first else ', '}}{{condition}}
            {% endfor %}
        {% endif %}
    """

    @classmethod
    def query(cls, table: str, columns: list[str] = ['*'],
              where: Optional[list[str]] = None,
              group_by: Optional[list[int]] = None):
        result = cls.conn.query(
            query=cls.query_base,
            params={
                'columns': columns,
                'table': table,
                'where': where,
                'group_by': group_by
            },
            template=False
        )
        return result
