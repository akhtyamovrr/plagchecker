#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include "alloc_matrix.h"
#include "Gauss_method.h"
#include "max_matrix_search.h"

/** 
@brief Перемещение строк в полученной матрице так, чтобы 
получилась единичная
@param[in] mat Матрица, содержащая не более одной единицы в столбце, 
остальные элементы нули
@param[in] n кол-во строк
Функция рассчитана на обработку конкретного типа матриц. В случае подачи
неподходящей матрицы результат перестановки строк может быть неверным 
или возможно зацикливание
*/
void remove_rows(double **mat, const int n)
{
	double eps = 0.0001;
	double *tmp = NULL;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			if (fabs(mat[i][j] - 1.0) < eps)
			{
				tmp = mat[i];
				mat[i] = mat[j];
				mat[j] = tmp;
			}	
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (fabs(mat[i][j] - 1.0) < eps && i != j)
				remove_rows(mat, n);
}

/**
@brief Функция реализует алгоритм Метода Гаусса с 
@param[in] mat исходная матриц
@param[in] n кол-во строк матрицы
@param[in] m кол-во столбцоа матрицы
@return Возвращает матрицу, преобразованную методом Гаусса
При подаче матрицы, размеры которой не удовлетворяют условию m-n = 1
или m == 0 || n == 0 возвращается NULL. Если mat == NULL, также возвращается
NULL
*/
double **gauss_method(double **mat, const int n, const int m)
{
	double *tmp;
	double eps = 0.001;
	int last = n - 1;
	int max_i;
	int max_j;
	int not_j[m];
	double arr[n]; // массив множителей
	if (m - n != 1 || n < 1)
		return NULL;
	if (!mat)
		return NULL;
	for (int i = 0; i < m; i++)
		not_j[i] = 0;
	for (int k = 0; k < n; k++)
	{
		max_pos_search(mat, last, m-1, &max_i, &max_j, not_j);
		if (fabs(mat[max_i][max_j] - 0) < eps)
		{
			remove_rows(mat, n);
			return mat;
		}
		// Ставим главную строку в конец
		if (max_i != last)
		{    
			tmp = mat[max_i];
		    mat[max_i] = mat[last];
		    mat[last] = tmp;
		}
		// Расчет коэффициентов
		for (int i = 0; i < n; i++)
			arr[i] = -mat[i][max_j] / mat[last][max_j];
		// Прибавление к каждой строке главной строки с учетом коэффициента
		assert(not_j[m-1] == 0);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (!not_j[j] && i != last)
					mat[i][j] += arr[i] * mat[last][j];
		// Поделим главную строку
		for (int j = 0; j < m; j++)
			if (j != max_j)
				mat[last][j] = mat[last][j] / mat[last][max_j];
		mat[last][max_j] = 1;
		// Запоминаем номер необрабатываемого столбца
		not_j[max_j] = 1;
		last--;
	}
	remove_rows(mat, n);
	return mat;
}