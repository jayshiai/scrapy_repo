#include <stdio.h>
#include <stdlib.h>

struct node
{
    int d;
    int c;

    struct node *next;
} node;

int arrange_node(struct node *h)
{
    int p;
    struct node *c = (struct node *)malloc(sizeof(struct node));
    struct node *s = h;

    for (; s->next != NULL; s = s->next)
    {
        c = s->next;
        for (; c->next != NULL; c = c->next)
        {
            if (s->d < c->d)
            {
                p = c->d;
                c->d = s->d;
                s->d = p;
                p = c->c;
                c->c = s->c;
                s->c = p;
            }
        }
    }
    printf("HERERERE");
    return 0;
}

int printlist(struct node *h)
{
    printf("HERERERE22222");
    struct node *s = h;
    for (; s->next != NULL; s = s->next)
    {
        printf("%dx^%d", s->c, s->d);
    }
    printf("\n");
    printf("HERERERE2222");
    return 0;
}

struct node *multiplypoly(struct node *h1, struct node *h2)
{
    printf("HERERERE3333");
    struct node *s = h1;
    struct node *h3;
    struct node *g = h2;
    struct node *t = (struct node *)malloc(sizeof(struct node));
    int c = 0;
    for (; s->next != NULL; s = s->next)
    {
        for (; g->next != NULL; g = g->next)
        {
            struct node *p = (struct node *)malloc(sizeof(struct node));
            t->next = p;

            p->d = g->d + s->d;
            p->c = g->c * s->c;
            t = p;
            if (c == 0)
                h3 = p;
            c++;
        }
    }
    s = h3;

    for (; s->next != NULL; s = s->next)
    {
        int c;
        t = s;
        for (; t->next != NULL; t = t->next)
        {
            if (s->d == t->d)
            {
                s->c = s->c + g->c;
                g->next = t->next;
                c = 0;
            }
            g = t;

            if (c = 0)
                free(t);
        }
    }
    printf("HERERERE3333");
    return h3;
}
int main()
{
    int c = 0;
    int cof, deg, n, m;

    printf("enter n");
    scanf("%d", &n);

    printf("enter m");
    scanf("%d", &m);
    struct node *s = (struct node *)malloc(sizeof(struct node));
    struct node *h1 = (struct node *)malloc(sizeof(struct node));
    for (int i = 1; i <= n; i++)
    {
        struct node *p = (struct node *)malloc(sizeof(struct node));
        s->next = p;
        printf("enter degree and coefficient for 1st poly");
        scanf("%d", &deg);
        scanf("%d", &cof);
        p->d = deg;
        p->c = cof;
        s = p;
        if (c == 0)
            h1 = p;
        c++;
    }
    struct node *h2;
    for (int i = 1; i <= m; i++)
    {
        struct node *p = (struct node *)malloc(sizeof(struct node));
        s->next = p;
        printf("enter degree and coefficient for 2nd poly");
        scanf("%d", &deg);
        scanf("%d", &cof);
        p->d = deg;
        p->c = cof;
        struct node *s = p;
        if (c == 0)
            h2 = p;
        c++;
    }
    // arrange_node(h1);
    // arrange_node(h2);

    struct node *h3 = multiplypoly(h1, h2);
    arrange_node(h3);

    printlist(h1);
    printlist(h2);
    printlist(h3);
    return 0;
}
