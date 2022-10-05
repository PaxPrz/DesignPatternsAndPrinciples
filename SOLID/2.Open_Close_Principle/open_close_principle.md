
# Open/Closed Principle

# Before

```mermaid
classDiagram
    class Order
    Order: +line_items
    Order: +shipping
    Order: +get_total()
    Order: +get_shipping_cost()
    Order: +get_arrival_date()
```

An class should be open for extension but closed for modification.
This is the motto of this principle. Here as we can see, if we need 
to add another shipping method in future let's say by 'waterways',
we need to update the Order class which is not a good way.

# After

```mermaid
classDiagram
    class Order
    Order: +line_items
    Order: +shipping#58; Shipping
    Order: +get_total()
    Order: +get_shipping_cost()
    Order: +get_arrival_date()

    class Shipping
    <<interface>> Shipping
    Shipping: +get_cost(order)
    Shipping: +get_arrival_date(order)

    class Ground
    Ground: +get_cost(order)
    Ground: +get_arrival_date(order)

    class Air
    Air: +get_cost(order)
    Air: +get_arrival_date(order)

    Order o-- Shipping
    Ground ..|> Shipping
    Air ..|> Shipping
```

Now here, shipping actually is an object that has all the
necessary functions defined using an interface (protocol).
If new shipping method are further added to the system, we now need
no modification in order class. Instead we implement Shipping interface
for our new 'waterways' shipping method