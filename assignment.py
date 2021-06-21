
Question 1 

list=[1,2,3,4]

def summ(num):

    sum= 0

    for i in num:

         sum+= i

    return sum

print(summ((list)))




Question 2

dict =	{
  "1": 50,
  "2": 60,
  "3": 70,
}
key = max(dict, key=dict.get) 
value = dict[key]

result = {

key:value

}
print(result)


Question 3

Answer

def getMaxLength(arr, n):
  
    # intitialize count
    count = 0 
      
    # initialize max
    result = 0 
  
    for i in range(0, n):
      
        if (arr[i] == 0):
            count = 0
  
        else:
              
            # increase count
            count+= 1 
            result = max(result, count) 
          
    return result

arr = [ 0, 0, 1, 0,1,1,1,0] 
n = len(arr) 
  
print(getMaxLength(arr, n))


Question 4 (a)

Answer

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `street` varchar(255) NOT NULL,
  `pincode` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_addresses` (`created_by_id`),
  CONSTRAINT `fk_addresses_created_by_id` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



Question 4 (b)

Answer

urlpatterns = [
    path('', RegistrationView, name='employee_insert'),
    path('list/',employee_list , name='employee_list'),
    path('delete/<int:id>',employee_delete, name ="employee_delete"),
    path('<int:id>/',employee_update,name='employee_update'),
    path('remove/<int:id>/', remove,name='remove'),
    path('login/',employee_login , name='employee_login'),

]
 
