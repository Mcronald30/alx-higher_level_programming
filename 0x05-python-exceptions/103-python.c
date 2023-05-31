#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic information
 * about Python lists.
 * @p: Python Object list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	setbuf(stdout, NULL);
	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 * print_python_bytes - Prints basic information
 * about Python byte objects.
 * @p: Python Object byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	char *bytes;
	PyBytesObject *bytesObj;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	setbuf(stdout, NULL);
	size = PyBytes_Size(p);
	bytesObj = (PyBytesObject *)p;
	bytes = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", bytes);

	if (size > 10)
		size = 10;

	printf("  [.] first %ld bytes: ", size);

	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)bytes[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic information
 * about Python float objects.
 * @p: Python Object float object.
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	setbuf(stdout, NULL);
	value = ((PyFloatObject *)p)->ob_fval;

	printf("[.] float object info\n");
	printf("  [.] value: %.17g\n", value);
}
