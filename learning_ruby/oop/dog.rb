class Animal
  def initialize(name,color)
    @name = name
    @color = color
  end
end 


class Dog < Animal
  def bark()
    puts "Woof"
  end
  
  def fetch(item)
    return item
  end

  def sit()
    puts @name + " sat down"
  end

  def stay()
    puts @name + " stayed still"
  end
end

d = Dog.new("Skippy","yellow")
d.bark()
d.bark()
d.stay()
d.sit()
puts d.fetch("stick")
