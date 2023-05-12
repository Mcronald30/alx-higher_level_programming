#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * print_python_list_info- Prints some basic info about Python lists.
 * @p: PyObject
 */

void print_python_list_info(__attribute__((unused)) PyObject *p)
{
	int item;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (item = 0; item < Py_SIZE(p); item++)
	{
		printf("Element %d: %s\n", item, Py_TYPE(PyList_GetItem(p, item))->tp_name);
	}
}
