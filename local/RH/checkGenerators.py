import mem_check as m
import random
import time

names = ['Sagar', 'Nandini', 'Abir', 'Souvik', 'Puki', 'Deblina']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print ('Memory (at start): {}Mb'.format(m.memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print ('Memory (at end) : {}Mb'.format(m.memory_usage_psutil()))
print ('Took {} Seconds'.format(t2-t1))