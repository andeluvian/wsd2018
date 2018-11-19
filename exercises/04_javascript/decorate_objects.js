var addPersonMethods = function (person){

var person = {};
person.name = name;
person.age = age;

console.log('Hi! I\'m ' + this.name + '.');



this.greet = function(sentence)
{
return sentence + ", my name is " + this.name
}

this.compareage = function(person){

if (this.age < person.age)
{
return "My name is " + this.name + " and I'm younger than " +person.name
}
if(this.age == person.age)
{
return "My name is " +this.name + " and I'm as young as " +person.name
}
else
{
return "My name is " +this.name + " and I'm older than " +person.name
}
}

this.namesake = function (person){

if(this.name == person.name){

  return "We have the same name, " + person.name + " and I!"
}
else
{
  return "We have different names, " + person.name + " and I."
}

}
};
