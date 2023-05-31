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
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		fflush(stdout);
		return;
	}

	setbuf(stdout, NULL);

	Py_ssize_t size = PyObject_Length(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, typeName);
	}
	fflush(stdout);
}

/**
 * print_python_bytes - Prints basic information
 * about Python byte objects.
 * @p: Python Object byte object.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		fflush(stdout);
		return;
	}

	setbuf(stdout, NULL);

	Py_ssize_t size = PyObject_Length(p);
	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", PyBytes_AsString(p));

	Py_ssize_t maxBytes = (size > 10) ? 10 : size;
	printf("  [.] first %ld bytes: ", maxBytes);

	for (Py_ssize_t i = 0; i < maxBytes; i++)
	{
		unsigned char byte = (unsigned char)PyBytes_AS_STRING(p)[i];
		printf("%02x", byte);
		if (i < maxBytes - 1)
		{
			printf(" ");
		}
	}

	printf("\n");
	fflush(stdout);
}

/**
 * print_python_float - Prints basic information
 * about Python float objects.
 * @p: Python Object float object.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		fflush(stdout);
		return;
	}

	setbuf(stdout, NULL);

	double value = ((PyFloatObject *)p)->ob_fval;

	printf("[.] float object info\n");
	printf("  [.] value: %.17g\n", value);
	fflush(stdout);
}
