#include <stdio.h>
#include "test.h"
int main(int argc, char **argv)
{
	Test<int, string> t {1, "test 1"};
	t.print();
	return 0;
}
