#include <include/Sorter.h>
namespace Coding2Challenge
{
template <class type1, class type2>
Sorter<type1, type2>::Sorter(std::vector<type1>& container1, const std::vector<type2>& container2,
                             std::function<bool(type2, type2)> comparator)
{

    auto element_c1 = container1.begin();
    auto element_c2 = container2.begin();
    while (element_c1 != container1.end() and element_c2 != container2.end())
    {
        containers_.push_back({*element_c1, *element_c2});
        ++element_c1;
        ++element_c2;
    }
    ExecuteSorting(comparator);
    UpdateContainer1(container1);
}

template <class type1, class type2>
Sorter<type1, type2>::Sorter(std::vector<type1>& container1, const std::vector<type2>& container2)
{

    auto element_c1 = container1.begin();
    auto element_c2 = container2.begin();
    while (element_c1 != container1.end() and element_c2 != container2.end())
    {
        containers_.push_back({*element_c1, *element_c2});
        ++element_c1;
        ++element_c2;
    }
    ExecuteSorting();
    UpdateContainer1(container1);
}
template <class type1, class type2> void Sorter<type1, type2>::UpdateContainer1(std::vector<type1>& output)
{
    int i = 0;
    for (auto element : containers_)
    {
        output[i] = element.container1_;
        ++i;
    }
}

template <class type1, class type2> void Sorter<type1, type2>::ExecuteSorting()
{
    std::sort(containers_.begin(), containers_.end(),
              [](auto left, auto rigth) { return left.container2_ < rigth.container2_; });
}

template <class type1, class type2>
void Sorter<type1, type2>::ExecuteSorting(std::function<bool(type2, type2)> comparator)
{
    std::function<bool(Containers, Containers)> comp = [comparator](Containers left, Containers rigth) {
        return comparator(left.container2_, rigth.container2_);
    };
    std::sort(containers_.begin(), containers_.end(), comp);
}

} // namespace Coding2Challenge