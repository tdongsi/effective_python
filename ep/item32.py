
import gc

found_objects = gc.get_objects()
print('%d objects before' % len(found_objects))

import waste_memory
x = waste_memory.run()

found_objects = gc.get_objects()
print('%d objects after' % len(found_objects))

