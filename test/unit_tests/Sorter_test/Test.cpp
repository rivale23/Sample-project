
#include <Sorter.h>
#include <cstdio>
#include <gtest/gtest.h>

namespace
{
class TestClass1
{
  public:
    TestClass1(double sample_value) : sample_member_variable{sample_value}
    {
    }
    double GetValue()
    {
        return sample_member_variable;
    }

  private:
    double sample_member_variable;
};

class TestClass2
{
  public:
    TestClass2(std::string sample_value) : sample_member_variable{sample_value}
    {
    }
    std::string GetValue()
    {
        return sample_member_variable;
    }

  private:
    std::string sample_member_variable;
};
} // namespace

TEST(CodeChallenge2Test, TestWithIntAsComparator)
{

    std::vector<std::string> container_1{"a", "b", "c", "d"};
    std::vector<int>         container_2{2, 4, 1, 3};

    std::vector<std::string> expected_values_after_sorting{"c", "a", "d", "b"};
    // Coding2Challenge::Sorter<std::string, int> sorter{container_1, container_2};

    EXPECT_EQ(container_1, expected_values_after_sorting);
}

TEST(CodeChallenge2Test, TestWithStringAsComparator)
{

    std::vector<int>         container_1{2, 4, 1, 3};
    std::vector<std::string> container_2{"z", "b", "c", "d"};

    std::vector<int> expected_values_after_sorting{4, 1, 3, 2};

    // Coding2Challenge::Sorter<int, std::string> sorter{container_1, container_2};

    EXPECT_EQ(container_1, expected_values_after_sorting);
}

TEST(CodeChallenge2Test, TestWithCustomClass_UsingLengthOfStringAsComparator)
{

    std::function<bool(TestClass2, TestClass2)> comparator = [](auto left, auto right) {
        return left.GetValue().length() < right.GetValue().length();
    };

    std::vector<TestClass1> container_testclass1 = {TestClass1(12), TestClass1(3), TestClass1(1), TestClass1(112)};
    std::vector<TestClass2> container_testclass2 = {TestClass2("abc"), TestClass2("a"), TestClass2("abcd"),
                                                    TestClass2("")};

    // Coding2Challenge::Sorter<TestClass1, TestClass2> sorter3{container_testclass1, container_testclass2, comparator};

    std::vector<TestClass1> expected_values_after_sorting = {TestClass1(112), TestClass1(3), TestClass1(12),
                                                             TestClass1(1)};

    ASSERT_EQ(container_testclass1[0].GetValue(), expected_values_after_sorting[0].GetValue());
    ASSERT_EQ(container_testclass1[1].GetValue(), expected_values_after_sorting[1].GetValue());
    ASSERT_EQ(container_testclass1[2].GetValue(), expected_values_after_sorting[2].GetValue());
    ASSERT_EQ(container_testclass1[3].GetValue(), expected_values_after_sorting[3].GetValue());
}

int main(int argc, char** argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
