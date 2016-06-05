class Parser
  def initialize(string)
    @string = string
  end

  def find_all(character)
    # Finds all the places of a character within a string
    indexes = []
    for val,ind in @string.split("").each_with_index
      if val == character
        indexes.push(ind)
      end
    end
    return indexes
  end

  def replace_all(character,new_character)
  #replaces all instances of a specific character with a new character
  end
end

p = Parser.new("Hello")
print p.find_all("l")
