// Define the Dog class
public class Dog {
    // Fields (also called attributes or properties)
    String color; //color of the dog
    String name;
    int age; //age of the dog

    // Constructor (runs when you create a new Dog)
    public Dog(String color, String name, int age) {
        this.color = color; // assign the parameter to the object's field
        this.name = name; // assign the parameter to the object's field
        this.age = age;
    }

    // Method (behavior): make the dog play
    public void play() {
        System.out.println(name + " is " + color + " and" + " he’s playing");
    }

    // Method to print dog info
    public void printInfo() {
        System.out.println("Dog's color: " + color);
        System.out.println("Dog's age: " + age + " years old");
        System.out.println("His name is: " + name);
    }
}
