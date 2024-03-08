#include "python.h"

/**
 * print_python_string - prints information about python strings.
 * @p: A pyObject string object.
 */
void print_python_string(pyObject *p)
{
	long int len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (tsrcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
