|[Return to Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## Metaclasses  

![](/assets/QQ0OK.png)

**Defined as “the class of a class”.**

* Any class whose instances are themselves classes.
* type is a metaclass for instance; it creates classes!
* Used to construct classes. \(always happens under hood\)
* Can create dynamic classes with less lines using type.
* Think: instances are to classes as classes are to metaclasses.
* To create a metaclass, create a class that inherits from type

```text
# in the most simple form
class Meta(type):
    pass
```

* Classes are normally created with the type metaclass
* We can create a class with a different metaclass:

```text
# Python 2
class Final(object):
    __metaclass__ = Meta
# Python 3
class Final(metaclass=Meta):
    pass
```

**\_\_new\_\_\(\):**  It’s a method which is called before \_\_init\_\_\(\). It creates the object and return it.

**\_\_init\_\_\(\):**  This method just initialize the created object passed as parameter

**Example:**

```text
class Meta(type):
    def __init__(cls, name, bases, dct):
        print "Creating class {} using Meta".format(name)
        super(Meta, cls).__init__(name, bases, dct)
class Foo(object):
    __metaclass__ = Meta
class FooBar(Foo):
    pass
```

First we create a new metaclass called **Meta**:

* On the construction of classes built using Meta, we print out that we are creating a class using Meta.

Next, create a class called Foo… built from Meta rather than type.

Finally, create a FooBar class from Foo.

* Notice how it too was built using Meta?

---

**End of Python Subject**

<a href="https://github.com/CyberTrainingUSAF/06-Intro-to-Algorithms/blob/master/00-Table-of-Contents.md" > Continue to Intro to Algorithms</a>

<a href="https://github.com/CyberTrainingUSAF/01-Course-Introduction-and-setup/blob/master/README.md" > Return to Course introduction </a>
