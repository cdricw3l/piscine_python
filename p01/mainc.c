/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mainc.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/17 03:39:56 by cdric.b           #+#    #+#             */
/*   Updated: 2026/03/20 15:17:36 by cdric.b          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <stdio.h>

#define abs(msg1, msg2) printf("hello %s\n", msg1, msg2)

int main(void)
{
    abs("world", 10);
    return (0);
}