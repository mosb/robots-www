class Complex1 {
        float _re, _im;
    public:
        Complex1(float re, float im)
        // : _re(re), _im(im)
        {
          _re = re;
          _im = im;
        }
        float real() const {
          return _re;
        }
        float imag() const {
          return _im;
        }
};


class Complex2 {
    public:
        float _re, _im;
        Complex2(float re, float im)
        {
          _re = re;
          _im = im;
        }
};


float mag1(const Complex1& c)
{
    return sqrt(c.real()*c.real() + c.imag()*c.imag());
}

Complex1 operator+(const Complex1& lhs, const Complex1& rhs)
{
    return Complex1(lhs.real() + rhs.real(), lhs.imag() + rhs.imag());
}

float mag2(const Complex2& c)
{
    return sqrt(c._re*c._re + c._im*c._im);
}

Complex2 operator+(const Complex2& lhs, const Complex2& rhs)
{
    return Complex2(lhs._re + rhs._re, lhs._im + rhs._im);
}

