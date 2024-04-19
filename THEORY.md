# Lesson 2. Шаблонизация 

Существует два типа меток в шаблонизаторе:
 1. <code>{% %}</code> - управляющие конструкции. Подключение, условия, циклы, включения. Например, для создания цикла внутри HTML-шаблона пишем так:
    <pre>{% for element in posledovatelnost %}
        action
    {% endfor %}</pre>
    Если нужно написать условие, то пишем так:
    <pre>{% if condition %}
        do this
    {% elif condition_2 %}
        do another
    {% else %}
        do another another
    {% endif %}
    </pre>
2. <code>{{ }}</code> - вставка значение переменных 
Работа с переменными внутри управляющих конструкций выглядит так: Например, нам нужно сгенерировать маркированный список, который будет состоять из элементов списка продуктов. 
Список продуктов генерируется в функции, которая занимается отображением (view).
У каждого продукта есть название, цена и ссылка на страницу с описанием 
этого продукта (поля в БД):

<pre>
from .models import Products

def products_page(request):
    prods = Products.objects.all()
    return render(request, 'prod_page.html', {'products': products})
</pre>
Когда view написана, можно перейти к оформлению шаблона страницы:
<pre>
...
&lt;ul&gt; &lt;!-- ставлю тег списка --&gt;
{% for pr in products %}  &lt;!-- циклом буду выводить все элементы на странице --&gt;
    &lt;li&gt;{{ pr }}&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
</pre>
Но, так как мне нужно вывести не только названия, а еще и цену, и ссылку, я напишу так:
<pre>
...
&lt;ul&gt;
{% for pr in products %} 
    &lt;li&gt;Продукт  &lt;a href="{{ pr.url }}"&gt;{{ pr.name }}&lt;/a&gt; {{ pr.price }} руб.&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
</pre>