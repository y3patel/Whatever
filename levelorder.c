#include<stdio.h>
#include<stdlib.h>

struct node
{
    int info;
    struct node *l;
    struct node *r;
};

struct node *head=NULL;
//const struct node *temp1 = head;


void myfun(int n, struct node *head)
{
    struct node *temp;
    temp = (struct node *)malloc(sizeof(struct node));
    temp->info=n;
    temp->l=NULL;
    temp->r=NULL;

    if(n < head->info)
    {
        if(head->l == NULL)
        {
            head->l=temp;
            return;
        }

        else
        {
            myfun(n,head->l);
        }
    }

    else if(n > head->info)
    {
        if(head->r == NULL)
        {
            head->r = temp;
            return;
        }
        else
        {
            myfun(n,head->r);
        }
    }
}

int height(struct node *head)
{
    if(head==NULL)
        return 0;
    else
        {
            int lheight = height(head->l);
            int rheight = height(head->r);

            if(lheight > rheight)
                return (lheight + 1);
            else
                return (rheight + 1);
        }

}

void printLevel(struct node *head,int level)
{
    if(head==NULL)
    {
       // printf("hii");
        return;
    }

    if(level==1)
    {
        printf("%d->",head->info);
    }
    else if(level > 1)
    {
        printLevel(head->l,level-1);
     //   printf("hii");
        printLevel(head->r,level-1);
    }
}

void printOrder(struct node *head)
{
    int h = height(head);
    int i;
    for(i=1;i<=h;i++)
    {
        printLevel(head,i);
    }
}



int main()
{
    int a,b,c,d,e,f,g,h,i,j;
    struct node *head = (struct node *)malloc(sizeof(struct node));
    printf("ENTER INFO ABOUT ROOT NODE\n");
    scanf("%d",&head->info);
    head->l=NULL;
    head->r=NULL;
   // show(head);
    scanf("%d",&b);
    scanf("%d %d %d %d %d %d %d %d",&c,&d,&e,&f,&g,&h,&i,&j);
    myfun(b,head);
    myfun(c,head);
    myfun(d,head);
    myfun(e,head);
    myfun(f,head);
    myfun(g,head);
    myfun(h,head);
    myfun(i,head);
    myfun(j,head);
    printOrder(head);
    return 0;
}

