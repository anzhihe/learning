#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int fac(int n)
{
    if (n < 2) return(1); /* 0! == 1! == 1 */
    return (n)*fac(n-1); /* n! == n*(n-1)! */
}

char *reverse(char *s)
{
    register char t,                    /* tmp */
            *p = s,                     /* fwd */
            *q = (s + (strlen(s) - 1)); /* bwd */

    while (p < q)               /* if p < q */
    {
        t = *p;         /* swap & move ptrs */
        *p++ = *q;
        *q-- = t;
    }
    return(s);
}

int main()
{
    char s[BUFSIZ];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", \
        reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", \
        reverse(s));
    return 0;
}
